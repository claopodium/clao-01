f1 = input("1复杂叶状体 2简单叶状体 3茎叶体")
if f1 == "1":
    print("地钱目 Marchantiales")
    s1 = input("颈卵器是否在特化的生殖托上？腹面是否有鳞片？（0 or 1）")
    if s1 == '1':
        print("地钱群 Marchatiatiineales")
        s2 = input("是否有气室气孔和鳞片？（0 or 1）")
        if s2 == '1':
            a1 =input("气孔为 0单式 1复式")
            if a1 == '0':
                a2 = input("0气室单层，无次级分隔 1气室多层，有次级分隔 ")
                if a2 == '0':    
                    l1 = input("是否是有绿色荧光的洞穴苔类，且气室不完整？（0 or 1）")
                    if l1 == '0':
                        v1 = input("气室营养丝是否发育且顶端细胞分化？（0 or 1）")
                        if v1 == '1':
                            f3 = input("植物体大，叶状体明显气室分隔（0 or 1）")
                            if f3 == '1':
                                print("蛇苔科 Conocephalaceae")
                            else:print("皮叶苔科 Tarhioniaceae")
                        else:print("花地钱科 Corsiniaceae")
                    else: print("光苔科 Cyatbodiaceae")
                else:s3 = input("气孔是否呈星形且椭圆形鳞片有狭长界限不明的附体？（1 or 0）")
                if s3 == '1':
                    print("星孔苔科 Sauteriaceae")
                else:print("石地钱科 Rebouliaceae")
            else: print("地钱科 Marchantiaceae 地钱属")
        else:print("地钱科 Marchantiaceae 毛地钱属 或 半月苔属")
    else:print("钱苔科 Ricciaceae")
elif f1 == "2":
    print("叶苔目 Jungermanniales 腋蒴叶苔亚目 Anacrogynineae")
    m1 = input("有无中肋？（0 or 1）")
    if m1 == '0':
        r1 = input("有无假根？（0 or 1）")
        if r1 == '0':
            print("片叶苔科 Aneuraceae")
        else:d1="边缘平直且精子器位于叶状体背面中部而非前端（0 or 1）"
        if d1 == "0":
            print("溪苔科 Pelliaceae")
        else:print("南溪苔科 Makinozaceae")
    else:c1 = input("植物体是否淡绿且透明？（0 or 1）")
    if c1 == '1':
        print("叉苔科 Mezggeriaceae")
    else:print("带叶苔科 Pallaviciniaceae")
elif f1 == "3":
    f2 = input("是否直立且有横走茎？（0 or 1）")
    if f2 == '0':
        print("顶蒴叶苔亚目 Acrogynineae")
        f4 = input("叶片排列形式为 1蔽前式 2折合蔽前式 3蔽后式 4折合蔽后式")
        if f4 != '2':
            print("叶苔群 Jungermanniineales")
            f5 = input("1.腹叶与侧叶近与同行或等大，为蔽前式，叶片多3-4裂，稀2裂或不裂" +"\n"+"2.腹叶不同形且较小甚至完全缺失，为蔽后式或折合蔽后式，叶片多2裂瓣，稀不裂或3-5裂 ")
            if f5== '1':
                print("毛叶苔亚群 Ptilidiinae")
                l2 = input("1.叶片分裂至基部、3-4深裂或成毛状"+"\n"+"2.叶片全缘，浅裂或深裂，绝不成毛状")
                if l2 == '1':
                    l3 = input("1叶片深裂成瓣"+"\n"+"2叶片呈细毛状")
                    if l3 == '1':
                        l4 = input("1.植物体棕色，叶细胞厚壁"+"\n"+"2.植物体绿色，呈细绒状，叶细胞薄壁")
                        if l4 == '1':
                            print("毛叶苔科 Ptilidiaceae")
                        else:print("绒苔科 Trichocoleaceae")
                    else:
                        l5=input("1.植物体纤小，无鞭状枝，裂瓣单列细胞"+"\n"+"2.植物体纤长，有鞭状枝，裂瓣不是单列细胞")
                        if l5 == '1':
                            print("睫毛苔科 Blepharostomaceae")
                        else:
                            l6=input("1.叶片2-4深裂，蒴萼发育"+"\n"+"2.叶片2深裂后各自再1-2深裂，蒴萼不发育")
                            if l6 == '1':
                                print("指叶苔科 Lepidoziaceae 细指苔属 Kurzia 或 皱指苔属 Telaranea")
                            else:print("复叉苔科 Lepicoleaceae")
                else:l7 = input("1.叶片横生，腹叶与侧叶近于等大同形，裂瓣往一侧偏斜，有假肋"+"\n"+"2.叶片斜列，腹叶与侧叶不等大或不同形，裂瓣不偏斜，无假肋")
                if l7 == '1':
                    print("剪叶苔科 Herbertacaceae")
                else:
                    l8 = input("1.分枝且有鞭状枝，叶片3-4裂"+"\n"+"2.不分枝且无鞭状枝，叶片全缘或尖部有2小裂瓣")
                    if l8 =='1':
                       print("指叶苔 Lepidoziaceae 指叶苔属 Lepidozia 或 细鞭苔属 Acromastigum 或 鞭苔属 Bazzania")
                    else:print("护蒴苔科 Calupogeiaceae")
            else:
                print("叶苔亚群 Jungermanniinae")
                v6=input("1.营养体扁平，无明显叶片"+"\n"+"2.营养体不扁平，常有明显叶片")
                if v6=='1':
                    v7=input("1.茎扁平，上凹下凸，有侧叶，无腹叶"+"\n"+"2.茎扁平虫形，梭形，无侧叶，有腹叶")
                    if v7 == '1':
                        print("塔叶苔科 Schiffneriaceae")
                    else:print("大萼苔科 Cephaloziaceae 虫叶苔属 Zoopsis")
                else:
                    l9=input("1.叶折合两裂瓣，背瓣小于腹瓣，腹叶完全缺失"+"\n"+"2.叶不折合，或虽有折合但背瓣不小于腹瓣，腹叶常有")
                    if l9 == '1':
                        l10 = input("1.叶片折合处无明显脊棱，腹瓣有明显侧生囊状结构"+"\n"+"2.叶片折合处有明显脊棱，腹瓣无明显侧生囊状结构")
                        if l10 == "1":
                            print("侧囊苔科 Delavayellaceae")
                        else:
                            l11=input("1.叶片折合处无背翅，蒴萼明显发育"+"\n"+"2.叶片折合处有明显背翅，蒴萼不发育")
                            if l11 == "1":
                                print("合叶苔科 Scapaniaceae")
                            else:print("歧舌苔科 Schistochilaceae")
                    else:
                        l12=("1.叶片对生，叶基背面多少连合"+"\n"+"2.叶片互生，叶基背面不连合")
                        if l12 =="1":
                            l13 = input("1.叶片密集，蒴萼不发育，有假孢蒴"+"\n"+"2.叶片稀疏，蒴萼发育")
                            if l13 == '1':
                                print("横叶苔科 Southbyaceae")
                            else:print("羽苔科 Plagiochilaceae 对羽苔属 Plagiochilion 和 对耳苔属 Syzygieila")
                        else:
                            r10=input("1.假根限于腹叶基部"+"\n"+"2.假根分散于茎的腹面")
                            if r10 == '1':
                                l14= input("1.侧叶圆形或方形，腹叶小于侧叶且两裂"+"\n"+"2.侧叶不为圆形或方形，腹叶小甚至缺失")
                                if l14 == '1':
                                    print("齿萼苔科 Lophocoleaceae")
                                else:print("羽苔科 Plagiochilaceae 小萼苔属 Mylia 或 羽苔属 Plagiochila")
                            else:
                                l15=input("1.叶片全缘，仅尖部微凹或有少数钝齿"+"\n"+"2.叶缘常有锯齿，叶片2-3裂，稀5裂")
                                if l15 == '1':
                                    s4 = input("1.植物体有横茎，多腹面分枝，蒴萼生于腹面的短枝上"+"\n"+"2.植物体无横茎，多侧生分枝，蒴萼生于茎、枝的顶端")
                                    if s4 == '1':
                                        print("裂齿苔科 Odontoschismaceae")
                                    else:
                                        l16=input("1.叶片原形或长方形，蒴萼筒形或背腹扁平"+"\n"+"2.叶片楔形或倒三角形，蒴萼两侧扁平")
                                        if l16 == '1':
                                            print("叶苔科 Jungermanniaceae")
                                        else:print("羽苔科 Plagiochilaceae 小萼苔属 Mylia 或 羽苔属 Plagiochila")
                                else:
                                    l17 = input("1.侧叶近于横生或横生"+"\n"+"2.侧叶斜列")
                                    if l17 =='1':
                                        l18 = input("1.叶2列，无腹叶，蒴萼不发育，代之以蒴周苞"+"\n"+"2.叶3列，有腹叶，蒴萼发育")
                                        if l18 == '1':
                                            print("钱袋苔科 Marsupeellaceae")
                                        else:
                                            l19 = input("1.植物体纤细，不超过1cm长，叶片稀疏排列，腹叶小或缺失"+"\n"+"2.植物体大，1-15cm长，叶密集排列，腹叶大")
                                            if l19 == '1':
                                                print("拟大萼苔科 Cephaloziellaceae")
                                            else:
                                                l20=input("1.叶片3-4深裂，边缘多齿"+"\n"+"2.叶片2裂，裂瓣全缘")
                                                if l20 =='1':
                                                    print("裂叶苔科 Lophpziaceae 广萼苔属 Chandonanthus")
                                                else:print("兔耳苔科 Antheliaceae")
                                    else:
                                        l21=input("1.叶片2-4裂，稀5裂，裂瓣全缘"+"\n"+"2.叶片不呈2-4裂，叶缘常有锯齿或缺刻")
                                        if l21 == '1':
                                            l23 = input("1.叶片2裂，有时后缘形成囊状，雌苞生于腹面短枝"+"\n"+"2.叶片2-5裂，雌苞生于茎枝顶端")
                                            if l23 == '1':
                                                print("大萼苔科 Cephaloziaceae")
                                            else:
                                                l24 = input("1.叶片2裂，蒴萼不发育，代之以蒴周苞或假蒴苞"+"\n"+"2.叶片2-5裂瓣，蒴萼发育")
                                                if l24 == '1':
                                                    print("叶苔科 Jungermanniaceae 被蒴苔属 Nardia")
                                                else:print("裂叶苔科 Lophoziaceae")
                                        else:
                                            l22 = input("1.植物体常有横茎及腹面分枝，叶片后缘内卷，雌雄苞均生于腹面短枝上，蒴萼膨大，不呈两侧扁平"+"/n"+"2.植物体常叉状分枝以及树状分枝，叶片前缘背卷，雄苞生于节间，雌苞生于茎枝顶端，蒴萼上部两侧扁平")
                                            if l22 == '1':
                                                print("隐蒴苔科 Adelanthaceae")
                                            else:print("羽苔科 Plagiochilaceae")
        else:
            print("毛耳苔群 Jubuliineales")
            v2 = input("有无腹叶？（0 or 1）")
            if v2 =='0':
                v3=input("腹瓣是否形成水囊？（0 or 1）")
                if v3 == '1':
                    print("紫叶苔科 Pleuroziaceae")
                else:r2 = input("1.假根生于腹瓣，腹瓣有齿，蒴萼扁平"+"\n"+"2.假根生于茎上，腹瓣无齿，蒴萼不为扁平")
                if r2 == '1':
                    print("扁萼苔科 Radulaceae")
                else:print("细鳞苔科 Lejeuneaceae 疣鳞苔亚科 Cololejeuneoideae")
            else:v4 = input("每（1 or 2）侧叶有一腹叶")
            if v4 == '2':
                print("细鳞苔科 Lejeuneaceae 双鳞苔亚科 Diplasiolejeuneoideae")
            else:v5 = input("腹叶（0不变化 1膨起成囊状 2变形成盔状、耳状）")
            if v5 == "1":
                print("细鳞苔科 Lejeuneaceae 皱萼苔亚科Ptychanthoideae 或 细鳞苔亚科 Lejeuneoideae")    
            elif v5 =="2":print("耳叶苔科 Frullaniaceae")
            elif v5 =="0":print("光萼苔科 Porellaceae")
    else: print('美苔亚目 Calobryinalees 美苔科 Calobryaceae')
