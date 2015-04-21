__author__ = 'Matheus Brasileiro Campos'

import zope.interface

class ISensor(zope.interface.Interface):
    """ An object that captures data from some kind of sensors. """

    def init(self):
        """ Initialize the sensor component. """

    def configure(self):
        """ Configures the sensor component accordingly to the sensor type. """

    def run(self):
        """ Starts the sensor component to captures data. """

    def finalize(self):
        """ Finalizes the sensor component. """

    def sendData(self):
        """ Sends new data provided by the sensor to local server. """