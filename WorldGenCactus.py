# package net.minecraft.src (Don't know how to translate this)
# Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
# Jad home page: http://www.kpdus.com/jad.html
# Decompiler options: packimports(3) braces deadcode 
# Translate from java to python by Leony

from random import randint
import WorldGenCactus
import isAirBlock
import canBlockStay
import setBlock
import boolean
import generate

class WorldGenCactus:

    WorldGenCactus()
    boolean.generate(World.world, Random.random, int.i, int.j, int.k)
        for x in (int.l == 0, l < 10, l+1):
            int.i1 = randint(0, 8) - randint(0, 8)
            int.j1 = randint(0, 4) - randint(0, 4)
            int.k1 = randint(0, 8) - randint(0, 8)
            if(isAirBlock(i1, j1, k1)):
                int.l1 = 1 + randint(randint(0, 3) + 1)
                for x in(int.i2 = 0; i2 < l1; i2+1):
                    if(canBlockStay(world, i1, j1 + i2, k1)):
                        setBlock(i1, j1 + i2, k1, Block.cactus.blockID)

        return true

