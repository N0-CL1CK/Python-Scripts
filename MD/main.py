import comb_sort
import quick_sort

from datetime import datetime as dt


def _repl(_string, _tuple, _replacer):
    for _item in _tuple:
        _string = _string.replace(_item, _replacer)
    return _string


def _get_array(_id):
    with open(f"array_with_{int(_id)*10**4}_elements.txt", "r") as _file:
        _str_array = _repl(_file.readlines()[0], ("[", "]", " "), "")
    _array = [int(_number) for _number in _str_array.split(",")]
    return _array


def _build_test(_test, _array):
    if _test == "quick sort":
        _init_time = dt.now()
        _array_sorted = quick_sort.sort(_array)
        _end_time = dt.now()
        _time_execution = (_end_time - _init_time)
        return _array_sorted, _time_execution

    elif _test == "comb sort":
        _init_time = dt.now()
        _array_sorted = comb_sort.sort(_array)
        _end_time = dt.now()
        _time_execution = (_end_time - _init_time)
        return _array_sorted, _time_execution
    else:
        return 0


def main():
    _quick_sort_results = {}
    _comb_sort_results = {}

    for _id in range(2, 11, 2):
        _array = _get_array(_id)
        _array_quick_sorted, _time_exec_quick = _build_test("quick sort", _array)
        _array_comb_sorted, _time_exec_comb = _build_test("comb sort", _array)
        print(f"[+INFO][Quick Sort] {_id*10**4} elementos executado em {_time_exec_quick.seconds} segundos e {_time_exec_quick.microseconds} microssegundos")
        print(f"[+INFO][Comb Sort] {_id*10**4} elementos executado em {_time_exec_comb.seconds} segundos e {_time_exec_comb.microseconds} microssegundos\n")
        _quick_sort_results.update({f"{_id*10**4} elementos": f"{_time_exec_quick.seconds} segundos e {_time_exec_quick.microseconds} microssegundos"})
        _comb_sort_results.update({f"{_id*10**4} elementos": f"{_time_exec_comb.seconds} segundos e {_time_exec_comb.microseconds} microssegundos"})

    with open("resultados.txt", "w") as _file:
        _file.write("Quick Sort Results:\n\n")
        for _key in _quick_sort_results.keys():
            _file.write(f"{_key} ordenados em {_quick_sort_results.get(_key)}\n")
        _file.write("\n\n\nComb Sort Results:\n\n")
        for _key in _comb_sort_results.keys():
            _file.write(f"{_key} ordenados em {_comb_sort_results.get(_key)}\n")

if __name__ == "__main__":
    main()
