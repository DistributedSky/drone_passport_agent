{ nixpkgs ? import ./fetchNixpkgs.nix { } }:

rec {
  package = nixpkgs.callPackage ./default.nix { };
}
