def solution(friends, gifts):
    scores = dict()
    
    for friend_out in friends:
        inner_dict = dict()
        for friend_in in friends:
            if friend_out != friend_in:
                inner_dict[friend_in] = 0
        inner_dict['sum_score'] = 0
        scores[friend_out] = inner_dict
    
    for gift in gifts:
        fr, to = gift.split()
        
        scores[fr][to] += 1
        scores[to][fr] -= 1
        scores[fr]['sum_score'] += 1
        scores[to]['sum_score'] -= 1
        
    gifts_dict = dict()
    for friend in friends:
        gifts_dict[friend] = 0
    
    for key_out, value_out in scores.items():
        for key_in, value_in in value_out.items():
            if key_in != 'sum_score':
                if value_in > 0:
                    gifts_dict[key_out] += 1
                elif value_in < 0:
                    continue
                else:
                    if scores[key_out]['sum_score'] > scores[key_in]['sum_score']:
                        gifts_dict[key_out] += 1
    
    return max([value for value in gifts_dict.values()])