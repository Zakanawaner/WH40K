# !python GetMesh.py <Name of the army>

import json
import os
import sys
import trimesh
import requests
import io
import re
import urllib.request


def main():
    if len(sys.argv) > 1:
        army = sys.argv[1]
        InJsonPath = './Source/TTSJSON/{}/'.format(army)

        if not os.path.exists('./Source/Dataoutput/{}'.format(army)):
            os.makedirs('./Source/Dataoutput/{}'.format(army))
        if not os.path.exists('./Source/MeshObjects/{}'.format(army)):
            os.makedirs('./Source/MeshObjects/{}'.format(army))
        if not os.path.exists('./Source/MeshObjects/{}/Mesh'.format(army)):
            os.makedirs('./Source/MeshObjects/{}/Mesh'.format(army))
        if not os.path.exists('./Source/MeshObjects/{}/Material'.format(army)):
            os.makedirs('./Source/MeshObjects/{}/Material'.format(army))

        OutMeshPath = './Source/Dataoutput/{}/mesh.txt'.format(army)
        OutObjMeshPath = './Source/MeshObjects/{}/Mesh/'.format(army)
        OutObjMaterialPath = './Source/MeshObjects/{}/Material/'.format(army)
    else:
        army = 'AdeptaSororitas'
        InJsonPath = './Source/TTSJSON/{}/'.format(army)

        if not os.path.exists('./Source/Dataoutput/{}'.format(army)):
            os.makedirs('./Source/Dataoutput/{}'.format(army))
        if not os.path.exists('./Source/MeshObjects/{}'.format(army)):
            os.makedirs('./Source/MeshObjects/{}'.format(army))
        if not os.path.exists('./Source/MeshObjects/{}/Mesh'.format(army)):
            os.makedirs('./Source/MeshObjects/{}/Mesh'.format(army))
        if not os.path.exists('./Source/MeshObjects/{}/Material'.format(army)):
            os.makedirs('./Source/MeshObjects/{}/Material'.format(army))

        OutMeshPath = './Source/Dataoutput/{}/mesh.txt'.format(army)
        OutObjMeshPath = './Source/MeshObjects/{}/Mesh/'.format(army)
        OutObjMaterialPath = './Source/MeshObjects/{}/Material/'.format(army)
    files = [json.load(open(InJsonPath + f))['ObjectStates'] for f in os.listdir(InJsonPath)]
    models = []
    for file in files:
        for unit in file:
            if unit['Nickname'] != '':
                models.append(unit)
    with open(OutMeshPath, 'w') as f:
        for i, model in enumerate(models):
            if 'CustomMesh' in model.keys():
                name = re.findall('([A-Z][a-z]*)', model['Nickname'])
                nickname = ''.join(name)
                f.write('{} = '.format(nickname) + '{\n')
                f.write('\t"name": "{}",'.format(nickname) + '\n')
                f.write('\t"scaleX": {},\n'.format(model['Transform']['scaleX']))
                f.write('\t"scaleY": {},\n'.format(model['Transform']['scaleY']))
                f.write('\t"MeshURL": "{}",\n'.format(str(model['CustomMesh']['MeshURL'])))
                f.write('\t"DiffuseURL": "{}"\n'.format(str(model['CustomMesh']['DiffuseURL'])))
                f.write('}\n')
                f.write('\n')
                f.write('\n')
                mesh = trimesh.load_mesh(file_obj=io.StringIO(requests.get(model['CustomMesh']['MeshURL']).
                                                              content.decode('utf-8')), file_type='obj')
                if not os.path.exists(OutObjMeshPath + '{}'.format(name[0])):
                    os.makedirs(OutObjMeshPath + '{}'.format(name[0]))
                mesh.export(OutObjMeshPath + '{}/{}.obj'.format(name[0], nickname + '_' + str(i)))
                if not os.path.exists(OutObjMaterialPath + '{}'.format(name[0])):
                    os.makedirs(OutObjMaterialPath + '{}'.format(name[0]))
                urllib.request.urlretrieve(model['CustomMesh']['DiffuseURL'],
                                           OutObjMaterialPath + '{}/{}.png'.format(name[0],
                                                                                   nickname + '_' + str(i)))
    f.close()


if __name__ == "__main__":
    main()
