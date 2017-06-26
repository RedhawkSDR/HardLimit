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
# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)
%{!?_sdrroot: %define _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}
Prefix:         %{_prefix}

# Point install paths to locations within our target SDR root
%define _sysconfdir    %{_prefix}/etc
%define _localstatedir %{_prefix}/var
%define _mandir        %{_prefix}/man
%define _infodir       %{_prefix}/info

Name:           rh.HardLimit
Version:        2.0.1
Release:        1%{?dist}
Summary:        Component %{name}

Group:          REDHAWK/Components
License:        LGPLv3+
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  redhawk-devel >= 2.0
Requires:       redhawk >= 2.0


# Interface requirements
BuildRequires:  bulkioInterfaces >= 2.0
Requires:       bulkioInterfaces >= 2.0

# Implementation java
Requires: java >= 1.6
BuildRequires: java-devel >= 1.6

# Allow upgrades from previous package name
Obsoletes:      HardLimit < 2.0.0


%description
Component %{name}
 * Commit: __REVISION__
 * Source Date/Time: __DATETIME__


%prep
%setup -q


%build
# Implementation cpp
pushd cpp
./reconf
%define _bindir %{_prefix}/dom/components/rh/HardLimit/cpp
%configure
make %{?_smp_mflags}
popd
# Implementation python
pushd python
./reconf
%define _bindir %{_prefix}/dom/components/rh/HardLimit/python
%configure
make %{?_smp_mflags}
popd
# Implementation java
pushd java
./reconf
%define _bindir %{_prefix}/dom/components/rh/HardLimit/java
%configure
make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
# Implementation cpp
pushd cpp
%define _bindir %{_prefix}/dom/components/rh/HardLimit/cpp
make install DESTDIR=$RPM_BUILD_ROOT
popd
# Implementation python
pushd python
%define _bindir %{_prefix}/dom/components/rh/HardLimit/python
make install DESTDIR=$RPM_BUILD_ROOT
popd
# Implementation java
pushd java
%define _bindir %{_prefix}/dom/components/rh/HardLimit/java
make install DESTDIR=$RPM_BUILD_ROOT
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,redhawk,redhawk,-)
%dir %{_prefix}/dom/components/rh/HardLimit
%{_prefix}/dom/components/rh/HardLimit/HardLimit.scd.xml
%{_prefix}/dom/components/rh/HardLimit/HardLimit.prf.xml
%{_prefix}/dom/components/rh/HardLimit/HardLimit.spd.xml
%{_prefix}/dom/components/rh/HardLimit/cpp
%{_prefix}/dom/components/rh/HardLimit/python
%{_prefix}/dom/components/rh/HardLimit/java

%changelog
* Wed Jun 21 2017 Ryan Bauman <rbauman@lgsinnovations.com> - 2.0.0-2
- Mass rebuild for REDHAWK 2.1.1

