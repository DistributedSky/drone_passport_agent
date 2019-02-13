{ nixpkgs ? import ./fetchNixpkgs.nix { } }:

rec {
  de_direct = nixpkgs.callPackage ./default.nix { };
}
