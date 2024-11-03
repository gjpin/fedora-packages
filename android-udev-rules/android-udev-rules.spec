Name:           android-udev-rules
Version:        20241019
Release:        1%{?dist}
Summary:        Android udev rules for better device handling

License:        GPLv3
URL:            https://github.com/M0Rf30/%{name}
Source0:        https://raw.githubusercontent.com/M0Rf30/android-udev-rules/refs/tags/%{version}/51-android.rules

BuildArch:      noarch
Requires(pre):  shadow-utils
Requires:       udev

%description
This package provides udev rules for Android devices to enable better USB handling
and ADB access.

%pre
getent group adbusers >/dev/null || groupadd -r adbusers
usermod -aG adbusers %{_username}

%install
mkdir -p %{buildroot}/etc/udev/rules.d
install -m 0644 %{SOURCE0} %{buildroot}/etc/udev/rules.d/51-android.rules

%post
udevadm control --reload
udevadm trigger

%files
%attr(644,root,root) /etc/udev/rules.d/51-android.rules

%changelog
* Mon Oct 28 2024 Package Maintainer <maintainer@example.com> - 20240328-1
- Initial package creation
- Added udev rules for Android devices
- Created adbusers group and user management