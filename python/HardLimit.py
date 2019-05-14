#!/usr/bin/env python
#
# This file is protected by Copyright. Please refer to the COPYRIGHT file distributed with this 
# source distribution.
# 
# This file is part of REDHAWK Basic Components HardLimit.
# 
# REDHAWK Basic Components HardLimit is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Lesser General Public License as published by the Free Software Foundation, either 
# version 3 of the License, or (at your option) any later version.
# 
# REDHAWK Basic Components HardLimit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along with this 
# program.  If not, see http://www.gnu.org/licenses/.
#
#
# AUTO-GENERATED
#
# Source: HardLimit.spd.xml
# Generated on: Tue Feb 12 16:55:08 EST 2013
# Redhawk IDE
# Version:M.1.8.2
# Build id: v201211201139RC3
from ossie.resource import Resource, start_component
import logging
import sys

from HardLimit_base import * 

class HardLimit_i(HardLimit_base):
    """Implements a high and low limit on the value of incoming data.  Values over the high limit will 
       be set to the high limit, values lower than the lower limit will be set to the low limit"""
       
    def initialize(self):
        """
        This is called by the framework immediately after your component registers with the NameService.
        
        In general, you should add customization here and not in the __init__ constructor.  If you have 
        a custom port implementation you can override the specific implementation here with a statement
        similar to the following:
          self.some_port = MyPortImplementation()
        """
        HardLimit_base.initialize(self)
        
        # TODO add customization here.
        

    def process(self):
        # Read the input data from the dataFloat_in port """
        data, T, EOS, streamID, sri, sriChanged, inputQueueFlushed = self.port_dataFloat_in.getPacket()
                
        if inputQueueFlushed:
            self._log.warning("input queue flushed - data has been thrown on the floor")
    
        # If no data is available then return NOOP which will sleep briefly and then call process() again    
        if data == None:
            return NOOP
        
        # Output sri equals the input sri for this component.  If anything is updated, then push that update out.  
        if sriChanged or not self.port_dataFloat_out.sriDict.has_key(streamID):
            self.port_dataFloat_out.pushSRI(sri);

        # Implement the hard limit logic
        for i, val in enumerate(data):
            if val > self.upper_limit:
                data[i] = self.upper_limit
            
            elif val < self.lower_limit:
                data[i] = self.lower_limit
        
        # Push the modified data out along with the T, EOS, and streamID we received in the input        
        self.port_dataFloat_out.pushPacket(data, T, EOS, streamID)
        
        # Since we did work then return NORMAL and thus call process() immediately  
        return NORMAL
        
  
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.WARN)
    logging.debug("Starting Component")
    start_component(HardLimit_i)

