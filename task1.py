def main():
    def convert(cel):
        if cel>=-273.15:
            kel=cel-273.15
            fahr=cel*9/5+32
            return round(kel,2), round(fahr,2)
        else:
            raise
            return
    cel=input('Enter degrees')
    try:
        cel=float(cel)
    except:
        print('Value error!!!')
    else:
        try:
            res_kel,res_fahr=convert(cel)
        except:
            print('Too low!!!')
        else:
            if res_kel==res_fahr:
                print('Too much!')
            else:
                print('kel:',res_kel,'\n fahr:',res_fahr)
    return
if __name__=='__main__':
    main()
