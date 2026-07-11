%global tl_name xprintlen
%global tl_revision 35928

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Print TeX lengths in a variety of units
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xprintlen
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xprintlen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xprintlen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a command, \printlen, to print TeX lengths in a
variety of units. It can handle all units supported by TeX. The package
requires that a reasonably up to date version of the fp package be
installed on you system.

