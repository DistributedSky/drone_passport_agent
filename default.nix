{ stdenv
, robonomics_comm
, mkRosPackage
, pkgs
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "drone_passport_agent";
  version = "0.2.2";

  src = ./.;

  propagatedBuildInputs = [ robonomics_comm pkgs.python37Packages.flask-restful ];

  meta = with stdenv.lib; {
    description = "DE direct";
    homepage = http://github.com/DroneEmployee/drone_passport_agent;
    license = licenses.bsd3;
    maintainers = [ maintainers.vourhey ];
  };
}
