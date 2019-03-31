import os
from astropy.table import Table


def load_AOS2015(galaxyname):
    outdict = dict()
    dir = '/test_data/optical+nir/'
    if galaxyname == "IZw18SE1":
        gname = 'IZw18SE1_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS0335-052E1":
        gname = 'SBS0335052E1_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS0335-052E3":
        gname = 'SBS0335052E3_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    # elif galaxyname == "J0519+0007":
    #     gname = ''
    #     T_OIII =
    #     full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS0940+5442":
        gname = 'SBS0940+5442_nir'
        T_OIII = 18600.0
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "Tol65":
        gname = 'Tol65_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS1415+437No13":
        gname = 'SBS1415+437No13_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS1415+437No2":
        gname = 'SBS1415+437No2_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "CGCG007-025No2":
        gname = 'CGCG007025No2_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "Mrk209":
        gname = 'Mrk209_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS1030+583":
        gname = 'SBS1030+583_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "Mrk71No1":
        gname = 'Mrk71No1_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS1152+579":
        gname = 'SBS1152+579_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "Mrk59":
        gname = 'Mrk59_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "SBS1135+581":
        gname = 'SBS1135+581_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    elif galaxyname == "Mrk450No1":
        gname = 'Mrk450No1_nir'
        T_OIII =
        full_tbl = Table.read(os.getcwd() + dir + gname, format='ascii', delimiter=' ')
    outdict["full_tbl"] = full_tbl
    outdict["T_OIII"] = T_OIII
    return outdict