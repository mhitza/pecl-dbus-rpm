# derivation spec file for php-pecl-dbus, based on the
# one provided by Remi Collet within the source rpm
# http://rpms.remirepo.net/SRPMS/php-pecl-dbus-0.1.1-2.remi.src.rpm
#
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/

Name:           pecl-dbus
Version:        0.1.1
Release:        1%{?dist}
Summary:        Extension for interaction with DBUS busses

License:        PHP
URL:            https://github.com/derickr/pecl-dbus
Source0:        %{name}-%{version}.tgz

BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  dbus-devel
BuildRequires:  libxml2-devel

%description
This extension allows you to talk to DBUS services on a system,
and also act as a DBUS service.


%prep
%autosetup
cat > pecl-dbus.ini << 'EOF'
extension=pecl-dbus.so
EOF


%build
phpize
%configure
%make_build

%install
mkdir -p %{buildroot}/usr/lib64/php/modules %{buildroot}/etc/php.d
install -m 0755 modules/dbus.so %{buildroot}/usr/lib64/php/modules/dbus.so
install -m 0644 pecl-dbus.ini %{buildroot}/etc/php.d/10-dbus.ini

%files
/usr/lib64/php/modules/dbus.so
%config(noreplace)
/etc/php.d/10-dbus.ini


%changelog
* Mon Dec 19 2022 Marius Ghita
- 
