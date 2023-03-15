Chaque personne à sa propre méthode pour faire de la veille technique.

Pour ma part, j'essaye de regrouper un maximum d'information à 1 seul endroit.

une grande partie des sites web ont un flux rss qui est mis à jour dès qu'une
news est publiée.

En utilisant un logiciel pouvant traquer ces flux, la veille est tout de suite
plus simple au quotidien.

Dans ce billet je vais vous présenter un outil que j'utilise pour faire
quotidiennement ma veille.

## Newsboat

Newsboat est un utilitaire en ligne de commande qui permet de traquer simplement
des flux rss/atom.

Pourquoi newsboat ? 

- pour sa simplicité à configurer
- pour la possibilité de ne jamais lever les mains du clavier :)
- parce qu'on peut utiliser les touches vim pour naviguer :D

## Configuration

La configuration de Newsboat se fait dans 2 fichiers : 

### ~/.config/newsboat/config (pour la configuration de newsboat)

Voici un exemple de configuration : 

	auto-reload yes
	reload-threads 100
	# display
	show-read-feeds no
	feed-sort-order unreadarticlecount-asc
	color info default default reverse
	color listnormal_unread yellow default
	color listfocus blue default reverse bold
	color listfocus_unread blue default reverse bold
	text-width 80
	# unbind keys
	unbind-key ENTER
	unbind-key j
	unbind-key k
	unbind-key J
	unbind-key K
	# bind keys - vim style
	bind-key j down
	bind-key k up
	bind-key l open
	bind-key h quit
	# highlights
	highlight article "^(Title):.*$" blue default
	highlight article "https?://[^ ]+" red default
	highlight article "\\[image\\ [0-9]+\\]" green default
	# open an internet link by typing on ENTER
	macro l set browser "open -a Safari %u"; open-in-browser ; set browser "links" define-filter "Starred" "flags = \"s\""
	macro i set browser "feh %u"; open-in-browser ; set browser "elinks %u"

### ~/.config/newsboat/urls (pour la configuration des flux)

Voici un exmple de configuration :

	https://tailscale.com/blog/index.xml
	https://www.hashicorp.com/blog/products/nomad/feed.xml
	https://news.ycombinator.com/rss
	https://www.exploit-db.com/rss.xml
	https://www.bsdnow.tv/rss
	https://github.blog/changelog/label/actions/feed/
	https://github.com/hashicorp/nomad/releases.atom

