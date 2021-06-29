// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile1 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile2 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile3 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile4 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile5 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level1":
            case "level1":return tiles.createTilemap(hex`3200080000000000000100000000030000000001000000000100000000010000000001000000000001000000000100000000010000040000000000010000000000000000000100000000010000000001000000000300000000000100000000030000000001000004000000000003000000000000000000030000000001000000000300000000000000000000030000000000000000000300000400000000000000000000000000000000000000000300000000000000000000000000000000000000000000000000000000040000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000400000000000200000000010000000002000000000000000000020000000002000000000000000000000200000000020000040505050505010505050501050505050105050505020505050501050505050105050505050205050505010505050501050504`, img`
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
`, [myTiles.transparency16,myTiles.tile2,myTiles.tile3,myTiles.tile4,myTiles.tile5,myTiles.tile1], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
            case "myTile":
            case "tile1":return tile1;
            case "myTile0":
            case "tile2":return tile2;
            case "myTile1":
            case "tile3":return tile3;
            case "myTile2":
            case "tile4":return tile4;
            case "myTile3":
            case "tile5":return tile5;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
