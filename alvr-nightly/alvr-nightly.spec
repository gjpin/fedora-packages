Name:           alvr-streamer
Version:        1.0
Release:        1%{?dist}
Summary:        ALVR Streamer - Prebuilt Linux binaries and libraries

License:        MIT
URL:            https://github.com/alvr-org/ALVR
Source0:        https://github.com/alvr-org/ALVR-nightly/releases/latest/download/alvr_streamer_linux.tar.gz

BuildArch:      x86_64
Requires:       firewalld

%description
ALVR Streamer provides Linux binaries and libraries required for running ALVR streaming services.

%prep
%autosetup -c -n alvr_streamer_linux

%build
# No build steps required since this package uses prebuilt binaries

%install
# Install binaries
install -Dm0755 bin/alvr_dashboard %{buildroot}%{_bindir}/alvr_dashboard

# Install libraries
install -Dm0755 lib64/libalvr_vulkan_layer.so %{buildroot}%{_libdir}/libalvr_vulkan_layer.so
install -Dm0644 lib64/alvr/driver.vrdrivermanifest %{buildroot}%{_libdir}/alvr/driver.vrdrivermanifest
install -Dm0755 lib64/alvr/bin/linux64/driver_alvr_server.so %{buildroot}%{_libdir}/alvr/bin/linux64/driver_alvr_server.so
install -Dm0755 lib64/alvr/bin/linux64/libopenvr_api.so %{buildroot}%{_libdir}/alvr/bin/linux64/libopenvr_api.so

# Install libexec files
install -Dm0644 libexec/alvr/alvr-firewalld.xml %{buildroot}%{_libexecdir}/alvr/alvr-firewalld.xml
install -Dm0755 libexec/alvr/alvr_drm_lease_shim.so %{buildroot}%{_libexecdir}/alvr/alvr_drm_lease_shim.so
install -Dm0755 libexec/alvr/alvr_fw_config.sh %{buildroot}%{_libexecdir}/alvr/alvr_fw_config.sh
install -Dm0755 libexec/alvr/ufw-alvr %{buildroot}%{_libexecdir}/alvr/ufw-alvr
install -Dm0755 libexec/alvr/vrcompositor-wrapper %{buildroot}%{_libexecdir}/alvr/vrcompositor-wrapper

# Install shared data
install -Dm0644 share/vulkan/explicit_layer.d/alvr_x86_64.json %{buildroot}%{_datadir}/vulkan/explicit_layer.d/alvr_x86_64.json

%files
%license LICENSE
%doc README.md
%{_bindir}/alvr_dashboard
%{_libdir}/libalvr_vulkan_layer.so
%{_libdir}/alvr/
%{_libexecdir}/alvr/
%{_datadir}/vulkan/explicit_layer.d/alvr_x86_64.json

%changelog
* Fri Jan 03 2025 Your Name <your.email@example.com> - 1.0-1
- Initial package
