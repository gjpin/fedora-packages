%global platform_tools_ver 35.0.2

Name:           android-platform-tools
Version:        %{platform_tools_ver}
Release:        1%{?dist}
Summary:        Android SDK Platform Tools

License:        Apache-2.0
URL:            https://developer.android.com/studio#command-tools
Source0:        https://dl.google.com/android/repository/platform-tools_r%{platform_tools_ver}-linux.zip

BuildRequires:  unzip
BuildArch:      x86_64

Requires:       java-latest-openjdk

%description
This package provides the Android SDK platform tools.

%prep
%setup -q -c -T
unzip %{SOURCE0}

%build
# Nothing to build

%install
# Create directory structure
mkdir -p %{buildroot}%{_prefix}/lib/android-sdk
mkdir -p %{buildroot}%{_bindir}

# Install platform tools
cp -a platform-tools %{buildroot}%{_prefix}/lib/android-sdk/

# Create symlinks for commonly used tools
ln -s %{_prefix}/lib/android-sdk/platform-tools/adb %{buildroot}%{_bindir}/adb
ln -s %{_prefix}/lib/android-sdk/platform-tools/fastboot %{buildroot}%{_bindir}/fastboot

# Set up environment variables
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/android-sdk.sh << 'EOF'
export ANDROID_HOME=%{_prefix}/lib/android-sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
EOF

%files
%{_prefix}/lib/android-sdk
%{_bindir}/adb
%{_bindir}/fastboot
%config(noreplace) %{_sysconfdir}/profile.d/android-sdk.sh

%post

%changelog
* Sun Nov 03 2024 Package Maintainer <maintainer@example.com> - 35.0.2-1
- Initial package
- Platform Tools version 35.0.2