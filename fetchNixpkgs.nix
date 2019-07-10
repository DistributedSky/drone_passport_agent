{ rev    ? "8b96d866aee52fd498b1b7c2509fbf1d05bda10b"             # The Git revision of nixpkgs to fetch
, sha256 ? "17mbbx4k17a1x7m41wj6m2wb33grq2nxn10p301q5niriwbrgiy2" # The SHA256 of the downloaded data
, system ? builtins.currentSystem                                 # This is overridable if necessary
}:

import (builtins.fetchTarball {
  url = "https://github.com/airalab/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}) { inherit system; }
