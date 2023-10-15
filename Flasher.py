# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QProcess
from enum import Enum


class FlasherState(Enum):
    Idle = 0
    Flash = 1
    BuildFS = 2
    Terminating = 3

class Flasher:
    def __init__(self, plainTextEdit):
        self._plainTextEdit = plainTextEdit
        self._state = FlasherState.Idle
        self._step_2_arguments = []
        self._finish_callback = None
        self._process = QProcess()
        self._process.readyReadStandardOutput.connect(self._handle_stdout)
        self._process.readyReadStandardError.connect(self._handle_stderr)
        self._process.finished.connect(self._handle_finished)

    def _log(self, msg):
        self._plainTextEdit.appendPlainText(msg)

    def _handle_stdout(self):
        msg = self._process.readAllStandardOutput().data().decode()
        self._log(msg)

    def _handle_stderr(self):
        msg = self._process.readAllStandardError().data().decode()
        self._log(msg)

    def _handle_finished(self, exitCode, exitStatus):
        prevState = self._state
        self._state = FlasherState.Idle

        if prevState == FlasherState.BuildFS:
            self._flash_fs_step_2(self._step_2_arguments)
        elif prevState == FlasherState.Flash or prevState == FlasherState.Terminating:
            if callable(self._finish_callback):
                self._finish_callback()

    def Flash(self, serialPort, baudrate, bootloaderPath='', partitionsPath='', boot_app0Path='', firmwarePath='', fsPath=''):
        if self._state != FlasherState.Idle:
            return

        if self._plainTextEdit.toPlainText() != '':
            self._log('-' * 128 + '\n')

        arguments = ['--chip', 'esp32s3']
        arguments.append('--port')
        arguments.append(serialPort)
        arguments.append('--baud')
        arguments.append(baudrate)
        arguments.extend(['--before', 'default_reset', '--after', 'hard_reset', 'write_flash', '-z', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '8MB'])
        if bootloaderPath != '':
            arguments.append('0x00000000')
            arguments.append(bootloaderPath)
        if partitionsPath != '':
            arguments.append('0x00008000')
            arguments.append(partitionsPath)
        if boot_app0Path != '':
            arguments.append('0x0000e000')
            arguments.append(boot_app0Path)
        if firmwarePath != '':
            arguments.append('0x00010000')
            arguments.append(firmwarePath)
        if fsPath != '':
            arguments.append('0x00670000')
            arguments.append(fsPath)

        self._state = FlasherState.Flash
        self._process.start('./venv/Scripts/esptool', arguments)

    def FlashFS(self, serialPort, baudrate, dir, imgPath):
        if self._state != FlasherState.Idle:
            return

        if self._plainTextEdit.toPlainText() != '':
            self._log('-' * 128 + '\n')

        arguments = ['-s', '1572864', '-p', '256', '-b', '4096']
        arguments.append('-c')
        arguments.append(dir)
        arguments.append(imgPath)

        self._state = FlasherState.BuildFS
        self._step_2_arguments.clear()
        self._step_2_arguments.extend([serialPort, baudrate, imgPath])
        self._process.start('./mklittlefs', arguments)

    def _flash_fs_step_2(self, arguments):
        if self._process.exitStatus() == QProcess.NormalExit and self._process.exitCode() == 0:
            self.Flash(arguments[0], arguments[1], fsPath=arguments[2])
        else:
            self._state = FlasherState.Flash
            self._handle_finished(self, self._process.exitStatus())

    def Terminate(self):
        if self._state == FlasherState.Idle:
            return

        self._state = FlasherState.Terminating
        self._process.terminate()

    def Kill(self):
        if self._state == FlasherState.Idle:
            return

        self._state = FlasherState.Terminating
        self._process.kill()

    def RegisterFinishCallback(self, cb):
        self._finish_callback = cb
