from services.serial import SerialComService
from constants import serial_command, serial_response

class RelayService():
  def __init__(self, serial_service: SerialComService):
    self.serial_service = serial_service

  def is_relay_on(self, relay_id: str) -> bool:
    return self.relay_status(relay_id) == serial_response.RELAY_ON

  def relay_on(self, relay_id: str):
    if not self.is_relay_on(relay_id):
      return self.toggle_relay(relay_id)
    return serial_response.SUCCESS

  def relay_off(self, relay_id: str):
    if self.is_relay_on(relay_id):
      return self.toggle_relay(relay_id)
    return serial_response.SUCCESS

  def toggle_relay(self, relay_id: str):
    c = serial_command.RELAY_TOGGLE[relay_id]
    resp = self.serial_service.request(c)
    return resp

  def relay_status(self, relay_id: str):
    c = serial_command.RELAY_STATUS[relay_id]
    resp = self.serial_service.request(c)
    return resp
  