camion = sprites.create(img("""
        ......44cc44........
            .....45555554.......
            ...4c5555555c5......
            ...4c1555555c54.....
            ..f551555555c5f.....
            ..f55155555555f.....
            ..f55155555555f.....
            ..f5c515155c55f.....
            ..45c5cccc5c554.....
            ..455cbbbbc4554.....
            ..455bbbbbb4554.....
            ..4444444444444.....
            ..444d444444d44.....
            ..4446d4444d644.....
            ..4444444444444.....
            ..4444444444444f....
            ..f444444444444f....
            ..ff4444444444ff....
            ...ff.......1ff.....
            ....................
    """),
    SpriteKind.player)
controller.move_sprite(camion)
tiles.place_on_tile(camion, tiles.get_tile_location(5, 50))
scene.camera_follow_sprite(camion)
luis = sprites.create(img("""
        . . . . . e e e e e . . . . . . 
            . . . . . f 1 d 1 f . . . . . . 
            . . . . . d d d d d . . . . . . 
            . . . . . d f f f d . . . . . . 
            . . . . . d 2 2 f d . . . . . . 
            . . . 4 4 4 4 4 4 4 4 4 . . . . 
            . . . 4 4 4 4 4 4 4 4 4 . . . . 
            . . . d d 4 4 4 4 4 d d . . . . 
            . . . d d 4 4 4 4 4 d d . . . . 
            . . . d d 4 4 4 4 4 d d . . . . 
            . . . d d 4 4 4 4 4 d d . . . . 
            . . . . . 4 4 4 4 4 . . . . . . 
            . . . . . 8 8 . 8 8 . . . . . . 
            . . . . . 8 8 . 8 8 . . . . . . 
            . . . . . 8 8 . 8 8 . . . . . . 
            . . . . . 8 8 . 8 8 . . . . . .
    """),
    SpriteKind.food)
pepe = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . f f f f . . . . . . . . 
            . . . . d d d d . . . . . . . . 
            . . . . f d d f . . . . . . . . 
            . . . . d f f d . . . . . . . . 
            . . . . d 2 f d . . . . . . . . 
            . . . 5 5 5 5 5 5 . . . . . . . 
            . . . d 5 5 5 5 d . . . . . . . 
            . . . d 5 5 5 5 d . . . . . . . 
            . . . . 8 8 8 8 . . . . . . . . 
            . . . . 8 8 8 8 . . . . . . . . 
            . . . . 8 . . 8 . . . . . . . . 
            . . . f f . . f f . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tiles.set_current_tilemap(tilemap("""
    level3
"""))
tiles.set_current_tilemap(tilemap("""
    level6
"""))