program exo4
    implicit none 
    character(len=15) :: fname,lname, adress, city, gender,country,street

    print*,"give me informations like that WITHOUT SPACE :"
    print*,"gender, first name, last name"
    read*,gender,fname,lname
    open(10,file="My_adress.txt")

    write(10,*)gender,".",fname," ",lname,","
    print*,"street,adress,city"
    read*,street,adress,city
    write(10,*)street,",",adress,",",city,","
    print*,"country"
    read*,country
    write(10,*)country
    close(10)
end program


