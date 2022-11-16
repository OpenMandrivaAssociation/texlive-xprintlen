Name:		texlive-xprintlen
Version:	35928
Release:	1
Summary:	Print TeX lengths in a variety of units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xprintlen
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xprintlen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xprintlen.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command, \printlen, to print TeX lengths
in a variety of units. It can handle all units supported by
TeX. The package requires that a reasonably up to date version
of the fp package be installed on you system.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xprintlen
%doc %{_texmfdistdir}/doc/latex/xprintlen

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
