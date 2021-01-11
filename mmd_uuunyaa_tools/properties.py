# -*- coding: utf-8 -*-
# Copyright 2021 UuuNyaa <UuuNyaa@gmail.com>
# This file is part of MMD UuuNyaa Tools.

import os
import glob

import bpy
import bpy.utils.previews
from mmd_uuunyaa_tools import material_tuner
from mmd_uuunyaa_tools import lighting_tuner


def load_previews():
    global previews
    previews = bpy.utils.previews.new()
    for path in glob.glob(os.path.join(os.path.dirname(__file__), 'thumbnails', '*.png')):
        previews.load(os.path.basename(path), path, 'IMAGE')


load_previews()


def update_lighting_thumbnails(property, context):
    bpy.ops.mmd_uuunyaa_tools.tune_lighting(lighting=property.thumbnails)


class LightingPropertyGroup(bpy.types.PropertyGroup):
    thumbnails: bpy.props.EnumProperty(
        items=lighting_tuner.TUNERS.to_enum_property_items(previews),
        description='Choose the lighting you want to use',
        update=update_lighting_thumbnails,
    )

    previous_collection_name: bpy.props.StringProperty()

    @staticmethod
    def register():
        bpy.types.Scene.mmd_uuunyaa_tools_lighting = bpy.props.PointerProperty(type=LightingPropertyGroup)

    @staticmethod
    def unregister():
        del bpy.types.Scene.mmd_uuunyaa_tools_lighting


def update_material_thumbnails(property, context):
    bpy.ops.mmd_uuunyaa_tools.tune_material(material=property.thumbnails)


class MaterialPropertyGroup(bpy.types.PropertyGroup):
    thumbnails: bpy.props.EnumProperty(
        items=material_tuner.TUNERS.to_enum_property_items(previews),
        description='Choose the material you want to use',
        update=update_material_thumbnails,
    )

    @staticmethod
    def register():
        bpy.types.Material.mmd_uuunyaa_tools_material = bpy.props.PointerProperty(type=MaterialPropertyGroup)

    @staticmethod
    def unregister():
        del bpy.types.Material.mmd_uuunyaa_tools_material
