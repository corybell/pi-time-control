from serial import Serial
from constants.serial_settings import BAUDRATE, TIMEOUT, WRITE_TIMEOUT, CHUNK_SIZE, ENCODING

class SerialComService():
  def __init__(self, serial_port: str):
    self.port = serial_port
    self.ser = None
    self.timer = None

  def request(self, data: str) -> str:
    self.__open()
    self.__write(data)
    response = self.__read()
    self.__close()
    return response

  def __open(self) -> str:
    self.ser = Serial(
      baudrate=BAUDRATE,
      port=self.port, 
      timeout=TIMEOUT,
      write_timeout=WRITE_TIMEOUT
    )
    
    return self.__read()

  def __close(self) -> None:
    self.ser.close()
    self.ser = None

  def __write(self, data: str) -> None:
    b = data.encode(ENCODING)
    self.ser.write(b)

  def __read(self) -> str:
    data = self.ser.read(CHUNK_SIZE)
    return data.decode(ENCODING)