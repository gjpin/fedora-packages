Name:           firefox-gnome-theme
Version:        131
Release:        1%{?dist}
Summary:        A GNOME theme for Firefox

License:        Unlicense
URL:            https://github.com/rafaelmardojai/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        INSTALL.md

BuildArch:      noarch

%description
A GNOME theme for Firefox that integrates Firefox into GNOME-based desktop environments.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/%{name}

# Install theme files
cp -ra theme userChrome.css userContent.css configuration %{buildroot}%{_libdir}/%{name}

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
install -pm 0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -pm 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/INSTALL.md

%files
%license LICENSE
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/INSTALL.md
%{_libdir}/%{name}

%changelog
* Sun Nov 03 2024 Package Maintainer <maintainer@example.com> - 131-1
- Initial package version