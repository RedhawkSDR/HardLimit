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

#ifndef STRUCTPROPS_H
#define STRUCTPROPS_H

/*******************************************************************************************

    AUTO-GENERATED CODE. DO NOT MODIFY

*******************************************************************************************/

#include <ossie/CorbaUtils.h>
#include <CF/cf.h>
#include <ossie/PropertyMap.h>
#include <ossie/OptionalProperty.h>
#include <ossie/AnyUtils.h>

struct Limits_struct {
    Limits_struct ()
    {
    };

    static std::string getId() {
        return std::string("Limits");
    };

    optional_property<float> upper_limit;
    optional_property<float> lower_limit;
};

inline bool operator>>= (const CORBA::Any& a, Limits_struct& s) {
    CF::Properties* temp;
    if (!(a >>= temp)) return false;
    redhawk::PropertyMap props(*temp);
    if (props.contains("Limits::upper_limit")) {
        if (!(ossie::any::isNull(props["Limits::upper_limit"]))) {
            float tmp;
            if (!(props["Limits::upper_limit"] >>= tmp)) return false;
            s.upper_limit = tmp;
        } else {
            s.upper_limit.reset();
        }
    }
    if (props.contains("Limits::lower_limit")) {
        if (!(ossie::any::isNull(props["Limits::lower_limit"]))) {
            float tmp;
            if (!(props["Limits::lower_limit"] >>= tmp)) return false;
            s.lower_limit = tmp;
        } else {
            s.lower_limit.reset();
        }
    }
    return true;
};

inline void operator<<= (CORBA::Any& a, const Limits_struct& s) {
    redhawk::PropertyMap props;
    if (s.upper_limit.isSet()) {
        props["Limits::upper_limit"] = *(s.upper_limit);
    }
    if (s.lower_limit.isSet()) {
        props["Limits::lower_limit"] = *(s.lower_limit);
    }
    a <<= props;
};

inline bool operator== (const Limits_struct& s1, const Limits_struct& s2) {
    if (s1.upper_limit!=s2.upper_limit)
        return false;
    if (s1.lower_limit!=s2.lower_limit)
        return false;
    return true;
};

inline bool operator!= (const Limits_struct& s1, const Limits_struct& s2) {
    return !(s1==s2);
};

#endif // STRUCTPROPS_H
