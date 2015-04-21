__author__ = 'Matheus Brasileiro Campos'

import zope.interface

class IAlert(zope.interface.Interface):
    """ An object that sends alerts to the alert device. """

    def init(self):
        """ Initialize the alert component. """

    def configure(self):
        """ Configures the alert component accordingly to the alert device. """

    def run(self):
        """ Starts the alert component to send alerts data. """

    def finalize(self):
        """ Finalizes the alert component. """

    def alert(self):
        """ Sends the data received from the local server to the alert device. """