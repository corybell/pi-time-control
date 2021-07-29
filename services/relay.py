from services.serial import SerialComService
from constants import serial_command, serial_response

class RelayService():
  def __init__(self, serial_service: SerialComService):
    self.serial_service = serial_service

  def relay_on(self, relay_id: str):
    command = serial_command.RELAY_ON.get(relay_id)
    if not command:
      return serial_response.BAD_REQUEST
    return self.serial_service.request(command)

  def relay_off(self, relay_id: str):
    command = serial_command.RELAY_OFF.get(relay_id)
    if not command:
      return serial_response.BAD_REQUEST;
    return self.serial_service.request(command)
  