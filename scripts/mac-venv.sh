#!/usr/bin/env bash
get_root_path() {
    local path; path="$(pwd)"
    path="${path%Data-Buccaneers*}Data-Buccaneers"
    printf '%s' "$path"
}

main() {
    local root_path; root_path="$(get_root_path)"
    local venv_path; venv_path="$root_path/.venv"
    cd "$root_path" || return
    
    if [[ ! -d "$venv_path" ]]; then
        python3 -m venv .venv
        source ./.venv/bin/activate
        if [[ -e ./TEXTrequirements.txt ]]; then
            pip3 install -r TEXTrequirements.txt
        fi
    else #venv exists, source it
        printf 'venv exists, source .venv/bin/activate'
    fi
}
main "$@"
