import os
while(True):
    os.system("clear")
    print("Choose and enter the option \n 1. Display storage devices\n 2. Display mounting points\n 3. Display Physical Volumes(PVs)\n 4. Display Volume Groups(VGs)\n 5. Display Logical Volumes(LVs)\n 6. Create Physical Volume(PV)\n 7. Create Volume Group(VG)\n 8. Create Logical Volume(LV)\n 9. Resize Logical Volume(LV)\n 10. Resize Volume Group(VG)\n 11. Remove Logical Volume(LV)\n 12. Remove Volume Group(VG)\n 13. Remove Physical Volume(PV)\n 14. Create file and display\n 15. Display file content")
    ch1=int(input(""))
    if(ch1 > 15 or ch1 < 2):
        exit
    if ch1 == 1:
        os.system("clear")
        os.system("fdisk -l")
    elif ch1 == 2:
        os.system("clear")
        os.system("df -hT")
    elif ch1 == 3:
        os.system("clear")
        pv = input("Enter the name of the PV or skip to view all PVs:  ")
        os.system("pvdisplay "+pv)
    elif ch1 == 4:
        os.system("clear")
        vg = input("Enter the name of the VG or skip to view all VGs:  ")
        os.system('vgdisplay '+vg)
    elif ch1 ==5:
        os.system("clear")
        lv = input("Enter the name of the LV or skip to view all LVs:  ")
        os.system('lvdisplay '+lv)
    elif ch1 == 6:
        os.system("clear")
        pv=input("Enter the location of the PV e.g. /dev/sbd:  ")
        os.system("pvcreate " + pv)
    elif ch1 == 7:
        os.system("clear")
        vg=input("Enter the name of the VG:  ")
        nopv=int(input("Enter the number of pv you want to form a VG:  "))
        createvg=""
        while(nopv!=0):
            os.system("clear")
            addvg=input("Enter the location of the PV:  ")
            createvg=createvg+" "+addvg
            nopv=nopv-1
        os.system("vgcreate " + vg +" " + createvg)
    elif ch1 == 8:
        os.system("clear")
        lv = input("Enter the name of the LV:  ")
        size=input("Enter the size of the LV:  ")
        vg=input("Enter the name of the VG:  ")
        os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
        ch2=1
        while(ch2!=0):
            os.system("clear")
            print("Enter yout choice: \n 1. Format the partition \n 2. Mount the partition \n 0. TO EXIT")
            ch2=int(input(""))
            if ch2== 1:
                os.system("mkfs.ext4 /dev/{}/{}".format(vg,lv))
            elif ch2 ==2:
                path=input("Enter the path andf name of the folder you want to mount  e.g. /home/user/folder_name:  ")
                os.system("mkdir "+path)
                os.system("mount /dev/{}/{} {}".format(vg,lv,path))
    elif ch1 == 9:
        os.system("clear")
        c = input("Enter the choice- Reduce/Extend the LV (R/E):  ")
        vg = input('Enter name of the VG in which  LV created: ')
        lv = input('Enter the name of LV you want to resize: ')
        if c == 'E':
            c='extend'
            s='+'
            size = input('Enter the size by which you want to extend LV size: ')
            os.system('lv{} --size {}{} /dev/{}/{}'.format(c,s,size,vg,lv))
            os.system('resize2fs /dev/{}/{}'.format(vg,lv))
        else:
            os.system("clear")
            size = input('Enter the size by which you want to change LV size: ')
            size2 = input('Enter the final reduced size of LV desired: ')
            path = input('Enter path to folder on which LV was mounted:  ')
            c='reduce'
            s='-'
            os.system('umount /dev/{}/{}'.format(vg,lv))
            os.system('e2fsck -f /dev/{}/{}'.format(vg,lv))
            os.system('resize2fs /dev/{}/{} {}'.format(vg,lv,size2))
            os.system('lv{} --size {}{} /dev/{}/{}'.format(c,s,size,vg,lv))
            os.system('mount /dev/{}/{} {}'.format(vg,lv,path))            
    elif ch1 == 10:
        os.system("clear")
        c = input("Enter the choice- Reduce/Extend the VG (R/E):  ")
        vg = input("Enter name of the VG:  ")
        if c == 'E':
            pv = input("Enter name of the PV:  ")
            os.system("vgextend {} {}".format(vg,pv))
        else:
            pv = input("Enter name of the PV:  ")
            os.system('pvmove {}'.format(pv))
            os.system('vgreduce {} {}'.format(vg,pv))
            print("DONE RESIZING!!!")
    elif ch1 == 11:
        os.system("clear")
        path = input('Enter path to LV you want to remove: ')
        os.system('umount {}'.format(path))
        os.system('lvremove {}'.format(path))
    elif ch1 == 12:
        os.system("clear")
        vg = input('Enter name of VG you want to remove: ')
        os.system('vgremove {}'.format(vg))
    elif ch1 == 13:
        os.system("clear")
        path = input('Enter path to PV you want to remove: ')
        os.system('pvremove {}'.format(path))
    elif ch1 == 14:
        os.system("clear")
        path = input('Enter the path to folder: ')
        file = input('Enter the filename: ')
        os.system('cat > {}/{}'.format(path,file))
        print('\nFile Created!')
        os.system('cat {}/{}'.format(path,file))
    elif ch1 == 15:
        os.system("clear")
        path = input('Enter the path to folder: ')
        file = input('Enter the filename: ')
        os.system('cat {}/{}'.format(path,file))	
    else:
        os.system("clear")
        print(">>>>>>>>>>>>>>>WRONG CHOICE<<<<<<<<<<<<<<<")
    input("Press Enter")