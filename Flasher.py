# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QProcess


class Flasher:
    def __init__(self, plainTextEdit):
        self._plainTextEdit = plainTextEdit
        self._process = QProcess()
        self._process.readyReadStandardOutput.connect(self._handle_stdout)
        self._process.readyReadStandardError.connect(self._handle_stderr)

    def _log(self, msg):
        self._plainTextEdit.appendPlainText(msg)

    def _handle_stdout(self):
        msg = self._process.readAllStandardOutput().data().decode()
        self._log(msg)

    def _handle_stderr(self):
        msg = self._process.readAllStandardError().data().decode()
        self._log(msg)

    def Flash(self, serialPort, baudrate, bootloaderPath='', partitionsPath='', boot_app0Path='', firmwarePath='', fsPath=''):
        if self._plainTextEdit.toPlainText() != '':
            self._log('-' * 128 + '\n')

        arguments = ['--chip', 'esp32s3', '--before', 'default_reset', '--after', 'hard_reset write_flash', '-z', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '8MB']
        arguments.append('--port')
        arguments.append(serialPort)
        arguments.append('--baud')
        arguments.append(baudrate)
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

        self.Terminate()
        self._process.start('esptool', arguments)

    def FlashFS(self, serialPort, baudrate, dir, imgPath):
        if self._plainTextEdit.toPlainText() != '':
            self._log('-' * 128 + '\n')

        arguments = ['-s', '1572864', '-p', '256', '-b', '4096']
        arguments.append('-c')
        arguments.append(dir)
        arguments.append(imgPath)

        self.Terminate()
        self._process.start('./mklittlefs', arguments)
        self._process.waitForFinished()
        self.Flash(self, serialPort, baudrate, fsPath=imgPath)

    def Terminate(self):
        self._process.terminate()
