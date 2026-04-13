{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.flask
    pkgs.python311Packages.pytz
    pkgs.python311Packages.ephem
  ];
}
