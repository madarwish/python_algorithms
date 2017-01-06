def getMinGroupCount(kidsAges , maxYearVar):
    if len(kidsAges) == 0:
        return 0
    elif len(kidsAges) == 1:
        return  1

    groupCount = 1
    startPoint = kidsAges[0]
    for i in kidsAges[1:]:
        if i - startPoint > maxYearVar:
            startPoint = i          
            groupCount = groupCount + 1
    return groupCount



def main():
    kidsAges = raw_input( ' Please provide the list of kids ages').split()
    print getMinGroupCount(sorted(map(float, kidsAges)) , 1 )
    return


if __name__ == '__main__':
    main()
