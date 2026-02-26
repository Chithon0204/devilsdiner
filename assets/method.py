

def recipe_calc(aa, ds):
    try:
        total_dough = aa*ds[list(ds.keys())[0]]
        key_list=list(ds.keys())
        values_list=list(ds.values())
        TOTAL_PERSENTAGE = sum(values_list[1:])
        main_ingredient_clac = total_dough / (1 + TOTAL_PERSENTAGE)
        ds[key_list[0]]=main_ingredient_clac
        for key in key_list[1:]:
            ds[key]=main_ingredient_clac*ds[key]
        return ds
    except Exception as e:
        print(f"Method file me error aa gya {e}")




