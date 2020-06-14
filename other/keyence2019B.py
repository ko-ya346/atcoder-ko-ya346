S=input()

ans='NO'
print(S.find('k'))
if S.find('k')==0 and S.rfind('eyence')==len(S)-6:
    ans='YES'
elif S.find('ke')==0 and S.rfind('yence')==len(S)-5:
    ans='YES'
elif S.find('key')==0 and S.rfind('ence')==len(S)-4:
    ans='YES'
elif S.find('keye')==0 and S.rfind('nce')==len(S)-3:
    ans='YES'
elif S.find('keyen')==0 and S.rfind('ce')==len(S)-2:
    ans='YES'
elif S.find('keyenc')==0 and S.rfind('e')==len(S)-1:
    ans='YES'

print(ans)
