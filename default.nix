{ stdenv
, robonomics_comm
, mkRosPackage
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "de_direct";
  version = "master";

  src = ./.;

  propagatedBuildInputs = [ robonomics_comm ];

  meta = with stdenv.lib; {
    description = "DE direct";
    homepage = http://github.com/vourhey/de_direct;
    license = licenses.bsd3;
    maintainers = [ maintainers.vourhey ];
  };
}
