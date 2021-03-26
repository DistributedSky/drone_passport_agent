{ stdenv
, robonomics_comm-nightly
, mkRosPackage
, pkgs
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "drone_passport_agent";
  version = "0.2.4";

  src = ./.;

  propagatedBuildInputs = [
    robonomics_comm-nightly
    pkgs.python3Packages.flask-restful
    pkgs.python3Packages.pinatapy
    pkgs.python3Packages.empy
    pkgs.python3Packages.ipfshttpclient
  ];

  meta = with stdenv.lib; {
    description = "DE direct";
    homepage = http://github.com/DroneEmployee/drone_passport_agent;
    license = licenses.bsd3;
    maintainers = [ maintainers.vourhey ];
  };
}
