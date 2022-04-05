# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:04:38 2022

@author: bywilson
"""
import connect

class create_shoulder_spare:
    
    def __init__(self):
        ##Look for POI's to use
        case = get_current("Case")
        examination = get_current("Examination")

        POI_name = 'Shoulder_Left_Spare'
        
        ##Create ROI from spherical expansion of POI
        
        
        ##Union the POI with 

if __name__ == '__main__':
    t = 1
    
    
    
# Script recorded 02 Mar 2022, 10:29:07

#   RayStation version: 10.0.1.52
#   Selected patient: ...

from connect import *



case.PatientModel.RegionsOfInterest['Spare_Shoulder_L'].CreateSphereGeometry(Radius=5, Examination=examination, Center={ 'x': 18.28125, 'y': 6.431875, 'z': -10.2 }, Representation="TriangleMesh", VoxelSize=None)

case.PatientModel.RegionsOfInterest['Spare_Shoulder_L'].CreateCylinderGeometry(Radius=5, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=5, Examination=examination, Center={ 'x': 18.28125, 'y': 6.431875, 'z': -10.2 }, Representation="TriangleMesh", VoxelSize=None)

case.PatientModel.RegionsOfInterest['NS_cylshoulder_L'].CreateCylinderGeometry(Radius=5, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=5, Examination=examination, Center={ 'x': 18.28125, 'y': 6.431875, 'z': -10.2 }, Representation="TriangleMesh", VoxelSize=None)

with CompositeAction('Update derived geometry (Spare_Shoulder_L, Image set: CT 1)'):

  case.PatientModel.RegionsOfInterest['Spare_Shoulder_L'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

  # CompositeAction ends 


retval_0 = case.PatientModel.CreatePoi(Examination=examination, Point={ 'x': -16.9921875, 'y': 7.2521875, 'z': -10.5 }, Name=r"Shoulder_Right_Spare", Color="Yellow", VisualizationDiameter=1, Type="DoseRegion")

case.PatientModel.RegionsOfInterest['NS_cylshoulder_R'].CreateCylinderGeometry(Radius=5, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=5, Examination=examination, Center={ 'x': -16.9921875, 'y': 7.2521875, 'z': -10.5 }, Representation="TriangleMesh", VoxelSize=None)

with CompositeAction('Update derived geometry (Spare_Shoulder_R, Image set: CT 1)'):

  case.PatientModel.RegionsOfInterest['Spare_Shoulder_R'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

  # CompositeAction ends 
