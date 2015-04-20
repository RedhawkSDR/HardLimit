/*
 * This file is protected by Copyright. Please refer to the COPYRIGHT file distributed with this 
 * source distribution.
 * 
 * This file is part of REDHAWK Basic Components HardLimit.
 * 
 * REDHAWK Basic Components HardLimit is free software: you can redistribute it and/or modify it under the terms of 
 * the GNU Lesser General Public License as published by the Free Software Foundation, either 
 * version 3 of the License, or (at your option) any later version.
 * 
 * REDHAWK Basic Components HardLimit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
 * PURPOSE.  See the GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License along with this 
 * program.  If not, see http://www.gnu.org/licenses/.
 */
package HardLimit.java;

import java.util.Properties;

import org.apache.log4j.Logger;

import org.omg.CosNaming.NamingContextPackage.CannotProceed;
import org.omg.CosNaming.NamingContextPackage.InvalidName;
import org.omg.CosNaming.NamingContextPackage.NotFound;
import org.omg.PortableServer.POAPackage.ServantNotActive;
import org.omg.PortableServer.POAPackage.WrongPolicy;

import CF.InvalidObjectReference;

import org.ossie.component.*;
import org.ossie.properties.*;


/**
 * This is the component code. This file contains all the access points
 * you need to use to be able to access all input and output ports,
 * respond to incoming data, and perform general component housekeeping
 *
 * Source: HardLimit.spd.xml
 *
 * @generated
 */

public abstract class HardLimit_base extends Component {
    /**
     * @generated
     */
    public final static Logger logger = Logger.getLogger(HardLimit_base.class.getName());

    /**
     * The property Limits
     * If the meaning of this property isn't clear, a description should be added.
     *
     * @generated
     */
    /**
     * The structure for property Limits
     * 
     * @generated
     */
    public static class Limits_struct extends StructDef {
        public final FloatProperty upper_limit =
            new FloatProperty(
                "Limits::upper_limit", //id
                "upper_limit", //name
                null, //default value
                Mode.READWRITE, //mode
                Action.EXTERNAL, //action
                new Kind[] {Kind.CONFIGURE}, //kind
                true
                );
        public final FloatProperty lower_limit =
            new FloatProperty(
                "Limits::lower_limit", //id
                "lower_limit", //name
                null, //default value
                Mode.READWRITE, //mode
                Action.EXTERNAL, //action
                new Kind[] {Kind.CONFIGURE}, //kind
                true
                );
    
        /**
         * @generated
         */
        public Limits_struct(Float upper_limit, Float lower_limit) {
            this();
            this.upper_limit.setValue(upper_limit);
            this.lower_limit.setValue(lower_limit);
        }
    
        /**
         * @generated
         */
        public Limits_struct() {
            addElement(this.upper_limit);
            addElement(this.lower_limit);
        }
    
        public String getId() {
            return "Limits";
        }
    };
    
    public final StructProperty<Limits_struct> Limits =
        new StructProperty<Limits_struct>(
            "Limits", //id
            "Limits", //name
            Limits_struct.class, //type
            new Limits_struct(), //default value
            Mode.READWRITE, //mode
            new Kind[] {Kind.CONFIGURE} //kind
            );
    
    // Provides/inputs
    /**
     * @generated
     */
    public bulkio.InFloatPort port_dataFloat_in;

    // Uses/outputs
    /**
     * @generated
     */
    public bulkio.OutFloatPort port_dataFloat_out;

    /**
     * @generated
     */
    public HardLimit_base()
    {
        super();

        // Properties
        addProperty(Limits);


        // Provides/inputs
        this.port_dataFloat_in = new bulkio.InFloatPort("dataFloat_in");
        this.addPort("dataFloat_in", this.port_dataFloat_in);

        // Uses/outputs
        this.port_dataFloat_out = new bulkio.OutFloatPort("dataFloat_out");
        this.addPort("dataFloat_out", this.port_dataFloat_out);
    }

    public void start() throws CF.ResourcePackage.StartError
    {
        super.start();
    }

    public void stop() throws CF.ResourcePackage.StopError
    {
        super.stop();
    }


    /**
     * The main function of your component.  If no args are provided, then the
     * CORBA object is not bound to an SCA Domain or NamingService and can
     * be run as a standard Java application.
     * 
     * @param args
     * @generated
     */
    public static void main(String[] args) 
    {
        final Properties orbProps = new Properties();
        HardLimit.configureOrb(orbProps);

        try {
            Component.start_component(HardLimit.class, args, orbProps);
        } catch (InvalidObjectReference e) {
            e.printStackTrace();
        } catch (NotFound e) {
            e.printStackTrace();
        } catch (CannotProceed e) {
            e.printStackTrace();
        } catch (InvalidName e) {
            e.printStackTrace();
        } catch (ServantNotActive e) {
            e.printStackTrace();
        } catch (WrongPolicy e) {
            e.printStackTrace();
        } catch (InstantiationException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }
}
