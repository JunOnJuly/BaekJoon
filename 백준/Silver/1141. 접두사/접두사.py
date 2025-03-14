S=sorted([input() for _ in range(int(input()))],key=lambda x:(len(x),x),reverse=True)
l=len(S)-1
while l:
    if any([S[s].startswith(S[l]) for s in range(len(S)) if s!=l]):del S[l];
    l-=1
print(len(S))