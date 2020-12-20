import numpy as np
import sim
import sys
import time

#-----Try to connect---------------
sim.simxFinish(-1)
your_IP='10.0.0.38'
clientID = sim.simxStart(your_IP,19997,True,True,10000,5)
if clientID != -1:    
    print("Connected to remote API server")
else:    
    print("Not connected to remote API server")   
    sys.exit ("could not connect")
     
#-----Start the Paused Simulation
err_code = sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot)

#Gantry Crane
err_code,CraneActuator = sim.simxGetObjectHandle(clientID,"CraneActuator",sim.simx_opmode_blocking)
err_code,CrabActuator1 = sim.simxGetObjectHandle(clientID,"CrabActuator1",sim.simx_opmode_blocking)
err_code,CrabActuator2 = sim.simxGetObjectHandle(clientID,"CrabActuator2",sim.simx_opmode_blocking)
err_code,LowerCrab1 = sim.simxGetObjectHandle(clientID,"LowerCrab1",sim.simx_opmode_blocking)
err_code,LowerCrab2 = sim.simxGetObjectHandle(clientID,"LowerCrab2",sim.simx_opmode_blocking)

#First Robot
err_code,Base_Spinner_1 = sim.simxGetObjectHandle(clientID,"Base_Spinner_1",sim.simx_opmode_blocking)
err_code,Link1_Link2_1 = sim.simxGetObjectHandle(clientID,"Link1_Link2_1",sim.simx_opmode_blocking)
err_code,Link2_Link3_1 = sim.simxGetObjectHandle(clientID,"Link2_Link3_1",sim.simx_opmode_blocking)
err_code,Link3_Link4_1 = sim.simxGetObjectHandle(clientID,"Link3_Link4_1",sim.simx_opmode_blocking)
err_code,Link4_Link5_1 = sim.simxGetObjectHandle(clientID,"Link4_Link5_1",sim.simx_opmode_blocking)
err_code,Link5_Link6_1 = sim.simxGetObjectHandle(clientID,"Link5_Link6_1",sim.simx_opmode_blocking)

#Second Robot
err_code,Base_Spinner_2 = sim.simxGetObjectHandle(clientID,"Base_Spinner_2",sim.simx_opmode_blocking)
err_code,Link1_Link2_2 = sim.simxGetObjectHandle(clientID,"Link1_Link2_2",sim.simx_opmode_blocking)
err_code,Link2_Link3_2 = sim.simxGetObjectHandle(clientID,"Link2_Link3_2",sim.simx_opmode_blocking)
err_code,Link3_Link4_2 = sim.simxGetObjectHandle(clientID,"Link3_Link4_2",sim.simx_opmode_blocking)
err_code,Link4_Link5_2 = sim.simxGetObjectHandle(clientID,"Link4_Link5_2",sim.simx_opmode_blocking)
err_code,Link5_Link6_2 = sim.simxGetObjectHandle(clientID,"Link5_Link6_2",sim.simx_opmode_blocking)


while True:    
    print("hello world")    
    a = np.transpose(np.asmatrix(np.linspace(1, -180, 500)))    
    print("a:")    
    print(a)    
    b = np.transpose(np.asmatrix(np.linspace(1, 180, 500)))    
    print("b:")    
    print(b)    
    c = np.transpose(np.asmatrix(np.linspace(1, 90, 500)))    
    print("c:")    
    print(c)    
    d = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))    
    print("d:")    
    print(d)    
    e = np.asmatrix(np.zeros((500, 1)))   
    print("e:")    
    print(e)    
    f = np.concatenate((d, b, a, e, c, d), axis=1)    
    print("f:")    
    print(f)  

    #Gantry Crane
    pos_val = 10 # in m
    err_code = sim.simxSetJointTargetPosition (clientID, CraneActuator,pos_val,sim.simx_opmode_streaming)
    time.sleep(1) #wait a short amount of time    
    
    pos_val = 5 # in m    
    err_code = sim.simxSetJointTargetPosition (clientID, CrabActuator1,pos_val,sim.simx_opmode_streaming)
    time.sleep(1) #wait a short amount of time    
    
    pos_val = 5 # in m   
    err_code = sim.simxSetJointTargetPosition (clientID, CrabActuator2,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = 2 # m  
    #robot.animate(stances=f, frame_rate=30, unit='deg')    
    err_code = sim.simxSetJointTargetPosition (clientID, LowerCrab1,pos_val,sim.simx_opmode_streaming)
    time.sleep(1) #wait a short amount of time    
    
    pos_val = 2 # in m    
    err_code = sim.simxSetJointTargetPosition (clientID, LowerCrab2,pos_val,sim.simx_opmode_streaming)
    time.sleep(1) #wait a short amount of time    
    

    #Robot 1
    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Base_Spinner_1,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link1_Link2_1,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link2_Link3_1,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link3_Link4_1,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link4_Link5_1,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link5_Link6_1,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time


    #Robot 2
    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Base_Spinner_2,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link1_Link2_2,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link2_Link3_2,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link3_Link4_2,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link4_Link5_2,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time

    pos_val = np.radians(40) # in degrees 0    
    err_code = sim.simxSetJointTargetPosition (clientID, Link5_Link6_2,pos_val,sim.simx_opmode_streaming) 
    time.sleep(1) #wait a short amount of time
