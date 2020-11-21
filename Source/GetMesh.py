# !python GetMesh.py <Name of the army>

import json
import os
import sys
import trimesh
import requests
import io
import urllib.request


def main():
    if len(sys.argv) > 1:
        army = sys.argv[1]
        InJsonPath = './Source/TTSJSON/{}/'.format(army)

        if not os.path.exists('./Source/Dataoutput/{}'.format(army)):
            os.makedirs('./Source/Dataoutput/{}'.format(army))
        if not os.path.exists('./Source/Objects/{}'.format(army)):
            os.makedirs('./Source/Objects/{}'.format(army))
        if not os.path.exists('./Source/Objects/{}/Mesh'.format(army)):
            os.makedirs('./Source/Objects/{}/Mesh'.format(army))
        if not os.path.exists('./Source/Objects/{}/Material'.format(army)):
            os.makedirs('./Source/Objects/{}/Material'.format(army))

        OutMeshPath = './Source/Dataoutput/{}/mesh.txt'.format(army)
        OutObjMeshPath = './Source/Objects/{}/Mesh/'.format(army)
        OutObjMaterialPath = './Source/Objects/{}/Material/'.format(army)
    else:
        army = 'Ultramarines'
        InJsonPath = './TTSJSON/{}/'.format(army)

        if not os.path.exists('./Dataoutput/{}'.format(army)):
            os.makedirs('./Dataoutput/{}'.format(army))
        if not os.path.exists('./Objects/{}'.format(army)):
            os.makedirs('./Objects/{}'.format(army))
        if not os.path.exists('./Objects/{}/Mesh'.format(army)):
            os.makedirs('./Objects/{}/Mesh'.format(army))
        if not os.path.exists('./Objects/{}/Material'.format(army)):
            os.makedirs('./Objects/{}/Material'.format(army))

        OutMeshPath = './Dataoutput/{}/mesh.txt'.format(army)
        OutObjMeshPath = './Objects/{}/Mesh/'.format(army)
        OutObjMaterialPath = './Objects/{}/Material/'.format(army)
    files = [json.load(open(InJsonPath + f))['ObjectStates'] for f in os.listdir(InJsonPath)]
    models = []
    for file in files:
        for unit in file:
            if unit['Nickname'] != '':
                models.append(unit)
    with open(OutMeshPath, 'w') as f:
        for i, model in enumerate(models):
            if 'CustomMesh' in model.keys():
                nickname = model['Nickname'].replace(' ', '').replace('-', '').replace('/', '').replace('+', '').replace('&', '').replace(' ', '')
                f.write('{} = '.format(nickname) + '{\n')
                f.write('\t"scaleX": {},\n'.format(model['Transform']['scaleX']))
                f.write('\t"scaleY": {},\n'.format(model['Transform']['scaleY']))
                f.write('\t"MeshURL": "{}",\n'.format(str(model['CustomMesh']['MeshURL'])))
                f.write('\t"DiffuseURL": "{}"\n'.format(str(model['CustomMesh']['DiffuseURL'])))
                f.write('}\n')
                f.write('\n')
                f.write('\n')
                mesh = trimesh.load_mesh(file_obj=io.StringIO(requests.get(model['CustomMesh']['MeshURL']).content.decode('utf-8')), file_type='obj')
                mesh.export(OutObjMeshPath + '{}.obj'.format(nickname + '_' + str(i)))
                urllib.request.urlretrieve(model['CustomMesh']['DiffuseURL'], OutObjMaterialPath + '{}.png'.format(nickname + '_' + str(i)))
    f.close()


if __name__ == "__main__":
    main()
