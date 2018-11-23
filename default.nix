{ stdenv
, ros_comm
, mkRosPackage
, python3Packages
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "de_direct";
  version = "master";

  src = ./.;

  propagatedBuildInputs = with python3Packages;
  [ ros_comm web3 multihash voluptuous ipfsapi ];

  meta = with stdenv.lib; {
    description = "DE direct";
    homepage = http://github.com/vourhey/de_direct;
    license = licenses.bsd3;
    maintainers = [ maintainers.vourhey ];
  };
}
