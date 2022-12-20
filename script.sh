#!/usr/bin/env sh

docker build -t rpmbuilder .

mkdir -p rpmbuild/BUILD rpmbuild/RPMS rpmbuild/SOURCES rpmbuild/SRPMS

wget https://github.com/derickr/pecl-dbus/archive/refs/heads/master.zip

unzip master.zip

mv pecl-dbus-master pecl-dbus-0.1.1
tar cf rpmbuild/SOURCES/pecl-dbus-0.1.1.tgz pecl-dbus-0.1.1

docker run --rm \
  -v `pwd`/rpmbuild:/root/rpmbuild:z \
  rpmbuilder \
  rpmbuild -ba /root/rpmbuild/SPECS/pecl-dbus.spec
