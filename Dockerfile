FROM fedora:37

RUN sudo dnf install -y rpmdevtools rpmlint

RUN sudo dnf install -y gcc php-devel dbus-devel libxml2-devel
