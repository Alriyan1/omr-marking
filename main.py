import cv2
import numpy as np
from utils import *

path='1.jpg'
wImg=700
hImg=700
Question=5
Choice=5
ans=[1,2,0,1,4]
webcamfeed=False


cap=cv2.VideoCapture(0)
cap.set(10,150)


while True:
    if webcamfeed:
        success,img=cap.read()
    else:
        img=cv2.imread(path)
    img=cv2.resize(img,(wImg,hImg))
    imgContours=img.copy()
    imgFinal=img.copy()
    imgBiggestContour=img.copy()
    imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGrey,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,10,50)

    try:

        contours,hierarchy=cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgContours,contours,-1,(0,225,0),7)

        rectCon=rectContour(contours)
        biggestContour=getCornerPoints(rectCon[0])
        gradePoints=getCornerPoints(rectCon[1])

        #print(biggestContour)

        if biggestContour.size!=0 and gradePoints.size!=0:
            cv2.drawContours(imgBiggestContour,biggestContour,-1,(0,255,0),20)
            cv2.drawContours(imgBiggestContour,gradePoints,-1,(255,0,0),20)
            biggestContour=reorder(biggestContour)
            gradePoints=reorder(gradePoints)

            pt1=np.float32(biggestContour)
            pt2=np.float32([[0,0],[wImg,0],[0,hImg],[wImg,hImg]])
            matrix=cv2.getPerspectiveTransform(pt1,pt2)
            imgWarpColored = cv2.warpPerspective(img,matrix,(wImg,hImg))

            ptg1=np.float32(gradePoints)
            ptg2=np.float32([[0,0],[325,0],[0,150],[325,150]])
            matrixg=cv2.getPerspectiveTransform(ptg1,ptg2)
            imgGradeDisplay = cv2.warpPerspective(img,matrixg,(325,150))
            #cv2.imshow('Grade',imgGradeDisplay)
            imgWrapGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
            imgThresh= cv2.threshold(imgWrapGray,170,255,cv2.THRESH_BINARY_INV)[1]

            boxes=splitBoxes(imgThresh)
            #cv2.imshow('test',boxes[2])

            #print(cv2.countNonZero(boxes[1]),cv2.countNonZero(boxes[2]))

            mypixelval=np.zeros((Question,Choice))
            countC=0
            countR=0
            for image in boxes:
                totalpixels=cv2.countNonZero(image)
                mypixelval[countR][countC]=totalpixels
                countC+=1
                if (countC==Choice):countC=0;countR+=1
            #print(mypixelval)

            myIndex=[]
            for x in range(Question):
                arr=mypixelval[x]
                #print(arr)
                myindexval=np.where(arr==np.amax(arr))
                #print(myindexval)
                myIndex.append(myindexval[0][0])
            #print(myIndex)

            grading=[]
            for x in range(Question):
                if ans[x]==myIndex[x]:
                    grading.append(1)
                else:
                    grading.append(0)
            #print(grading)
            score=(sum(grading)/Question) * 100
            #print(score)

            imgResult=imgWarpColored.copy()
            imgResult=showAnswer(imgResult,myIndex,grading,ans,Question,Choice)

            imRawDrawing=np.zeros_like(imgWarpColored)
            imRawDrawing=showAnswer(imRawDrawing,myIndex,grading,ans,Question,Choice)

            invmatrix=cv2.getPerspectiveTransform(pt2,pt1)
            imginvwarp = cv2.warpPerspective(imRawDrawing,invmatrix,(wImg,hImg))

            imgRawGrade = np.zeros_like(imgGradeDisplay)
            cv2.putText(imgRawGrade,str(int(score))+'%',(60,100),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),8,lineType=cv2.LINE_AA)
            cv2.putText(imgRawGrade,str(int(score))+'%',(60,100),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),4)
            invmatrixg=cv2.getPerspectiveTransform(ptg2,ptg1)
            imginvGradeDisplay = cv2.warpPerspective(imgRawGrade,invmatrixg,(wImg,hImg))

            imgFinal=cv2.addWeighted(imgFinal,.7,imginvwarp,.7,0)
            imgFinal=cv2.addWeighted(imgFinal,.7,imginvGradeDisplay,.7,0)



        imgBlank=np.zeros_like(img)

        stacked=([img,imgGrey,imgBlur,imgCanny],
                [imgContours,imgBiggestContour,imgWarpColored,imgThresh],
                [imgResult,imRawDrawing,imginvwarp,imgFinal])
        
    except:
        imgBlank=np.zeros_like(img)

        stacked=([img,imgGrey,imgBlur,imgCanny],
                [imgBlank,imgBlank,imgBlank,imgBlank],
                [imgBlank,imgBlank,imgBlank,imgBlank])
        
    lables = [["Original","Gray","Edges","Contours"],
                ["Contour","Biggest con","Warp","Threshold"],
                ['Results','Raw Drawing','Inv wrap','Final']]

    stacked_imgs=stackImages(stacked,0.4)

    cv2.imshow('final image',imgFinal)
    #cv2.imshow('original',stacked_imgs)
    
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        break