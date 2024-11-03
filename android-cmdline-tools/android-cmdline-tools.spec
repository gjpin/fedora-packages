%global cmdline_tools_ver 11076708

Name:           android-cmdline-tools
Version:        %{cmdline_tools_ver}
Release:        1%{?dist}
Summary:        Android SDK Command-line Tools

License:        Apache-2.0
URL:            https://developer.android.com/studio#command-tools
Source0:        https://dl.google.com/android/repository/commandlinetools-linux-%{cmdline_tools_ver}_latest.zip

BuildRequires:  unzip
BuildArch:      x86_64

Requires:       java-latest-openjdk

%description
This package provides the Android SDK command-line tools.

%prep
%setup -q -c -T
unzip %{SOURCE0}

%build
# Nothing to build

%install
# Create directory structure
mkdir -p %{buildroot}%{_prefix}/lib/android-sdk
mkdir -p %{buildroot}%{_bindir}

# Install command-line tools
cp -a cmdline-tools %{buildroot}%{_prefix}/lib/android-sdk/

# Set up environment variables
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/android-sdk.sh << 'EOF'
export ANDROID_HOME=%{_prefix}/lib/android-sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
EOF

%files
%{_prefix}/lib/android-sdk
%{_bindir}/adb
%{_bindir}/fastboot
%config(noreplace) %{_sysconfdir}/profile.d/android-sdk.sh

%post
# Set up cmdline-tools/latest symlink
if [ ! -e %{_prefix}/lib/android-sdk/cmdline-tools/latest ]; then
    cd %{_prefix}/lib/android-sdk/cmdline-tools
    ln -s ./* latest
fi

%changelog
* Sun Nov 03 2024 Package Maintainer <maintainer@example.com> - 11076708
- Initial package
- Command-line Tools version 11076708