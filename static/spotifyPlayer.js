window.onSpotifyWebPlaybackSDKReady = () => {
    // var token = "BQCCx9lpjrViiy5JiP7_pEwGsNAUOjAet9ADCdDN6cIYgFLYpJZiSuPuXzyvRKt9LteFgEQCRwpI2QlmdbPsTe4JrV6jYA8koZRYbYzBdVQTDyrTi9HiTXQXHMPGV3DIH7BKgVi1NpJ-rd-oTuILcMWcw4Cy2drBRqzDrZ7fuapXkDUIEVNIjdw";
    const accessToken = '{{token.userToken}}';
    const player = new Spotify.Player({
      name: 'Web Playback SDK Quick Start Player',
      getOAuthToken: cb => { cb(accessToken); }
    });

    // Error handling
    player.addListener('initialization_error', ({ message }) => { console.error(message); });
    player.addListener('authentication_error', ({ message }) => { console.error(message); });
    player.addListener('account_error', ({ message }) => { console.error(message); });
    player.addListener('playback_error', ({ message }) => { console.error(message); });

    // Playback status updates
    player.addListener('player_state_changed', state => { console.log(state); });

    // Ready
    player.addListener('ready', ({ device_id }) => {
      console.log('Ready with Device ID', device_id);
    });

    // Not Ready
    player.addListener('not_ready', ({ device_id }) => {
      console.log('Device ID has gone offline', device_id);
    });

    // Connect to the player!
    player.connect();
  };