{ stdenv
, robonomics_comm
, mkRosPackage
, pkgs
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "de_direct";
  version = "0.1.0";

  src = ./.;

  propagatedBuildInputs = [ robonomics_comm pkgs.python37Packages.flask-restful ];

  meta = with stdenv.lib; {
    description = "DE direct";
    homepage = http://github.com/DroneEmployee/de_direct;
    license = licenses.bsd3;
    maintainers = [ maintainers.vourhey ];
  };
}
