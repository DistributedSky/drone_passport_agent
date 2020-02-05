{ rev    ? "939f58402257c9c4b527bddf74efe67b68cbbfe8"             # The Git revision of nixpkgs to fetch
, sha256 ? "1w7w2pc5msqsfp0dq0x80rri8hhwdfvz5r8hm53qp7nir6f2fx9i" # The SHA256 of the downloaded data
, system ? builtins.currentSystem                                 # This is overridable if necessary
}:

import (builtins.fetchTarball {
  url = "https://github.com/airalab/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}) { inherit system; }
